import fs from 'fs';
import path from 'path';

const copyRecursive = (src, dest) => {
  if (!fs.existsSync(src)) return;
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
};

const root = process.cwd();
const appStatic = path.join(root, 'app', 'static');
const publicStatic = path.join(root, 'public', 'static');
const publicImages = path.join(root, 'public', 'images');

console.log('Copying static assets for production...');
copyRecursive(appStatic, publicStatic);

if (fs.existsSync(path.join(appStatic, 'images'))) {
  copyRecursive(path.join(appStatic, 'images'), publicImages);
}

console.log('Static assets synced to public/ directory successfully.');
