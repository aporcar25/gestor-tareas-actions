const fs = require('node:fs');

const archivos = ['README.md', 'LICENSE', 'CONTRIBUTING.md'];
let faltan = 0;

for (const archivo of archivos) {
  if (fs.existsSync(archivo)) {
    console.log(`OK: existe ${archivo}`);
  } else {
    console.error(`ERROR: falta ${archivo}`);
    faltan++;
  }
}

if (faltan > 0) {
  console.error(`ERROR: faltan ${faltan} archivo(s) de documentación`);
  process.exitCode = 1;
} else {
  console.log('Toda la documentación necesaria existe');
}