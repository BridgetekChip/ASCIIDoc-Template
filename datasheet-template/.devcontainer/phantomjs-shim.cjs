#!/usr/bin/env node

const fs = require('fs/promises');
const path = require('path');

function printVersion() {
  console.log('phantomjs shim 1.0.0 (chromium + wavedrom)');
}

function parseArgs(argv) {
  if (argv.length === 1 && (argv[0] === '--version' || argv[0] === '-v')) {
    return { version: true };
  }

  const args = {
    input: null,
    svg: null,
    png: null,
  };

  let i = 0;
  if (argv[i] && !argv[i].startsWith('-')) {
    i += 1;
  }

  for (; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '-i' && i + 1 < argv.length) {
      args.input = argv[++i];
    } else if (arg === '-s' && i + 1 < argv.length) {
      args.svg = argv[++i];
    } else if (arg === '-p' && i + 1 < argv.length) {
      args.png = argv[++i];
    } else if (arg === '--version' || arg === '-v') {
      args.version = true;
    }
  }

  return args;
}

function usage() {
  console.error('Usage: phantomjs <ignored-tool> -i input.json5 (-s output.svg | -p output.png)');
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.version) {
    printVersion();
    return;
  }

  if (!args.input || (!args.svg && !args.png)) {
    usage();
    process.exitCode = 1;
    return;
  }

  const { chromium } = require('playwright-core');
  const wavedromPkg = path.dirname(require.resolve('wavedrom/package.json'));
  const skinPath = path.join(wavedromPkg, 'skins', 'default.js');
  const libPath = path.join(wavedromPkg, 'wavedrom.min.js');
  const inputSource = await fs.readFile(args.input, 'utf8');
  const htmlSource = inputSource.replace(/<\/script>/gi, '<\\/script>');
  const executablePath = process.env.CHROMIUM_EXECUTABLE || '/usr/bin/chromium';

  const browser = await chromium.launch({
    executablePath,
    args: ['--headless=new', '--disable-gpu', '--no-sandbox'],
  });

  try {
    const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
    await page.setContent(
      `<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      html, body { margin: 0; padding: 0; background: #ffffff; }
      body { display: inline-block; }
      #container { display: inline-block; padding: 0; }
      svg { display: block; }
    </style>
  </head>
  <body>
    <div id="container">
      <script type="WaveDrom">${htmlSource}</script>
    </div>
  </body>
</html>`,
      { waitUntil: 'domcontentloaded' }
    );
    await page.addScriptTag({ path: skinPath });
    await page.addScriptTag({ path: libPath });
    await page.evaluate(() => {
      WaveDrom.ProcessAll();
    });
    await page.waitForSelector('svg');

    const svgMarkup = await page.$eval('svg', (element) => {
      const serializer = new XMLSerializer();
      return serializer.serializeToString(element);
    });

    if (args.svg) {
      await fs.mkdir(path.dirname(args.svg), { recursive: true });
      await fs.writeFile(args.svg, `${svgMarkup}\n`, 'utf8');
    }

    if (args.png) {
      const svg = await page.$('svg');
      const box = await svg.boundingBox();
      const clip = {
        x: 0,
        y: 0,
        width: Math.ceil(box.width),
        height: Math.ceil(box.height),
      };
      await fs.mkdir(path.dirname(args.png), { recursive: true });
      await page.screenshot({ path: args.png, clip });
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error && error.stack ? error.stack : String(error));
  process.exitCode = 1;
});
