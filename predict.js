// predict.js
const tf = require('@tensorflow/tfjs-node');
const fs = require('fs');

async function loadModel() {
    const model = await tf.loadGraphModel('model.json');
    return model;
}

async function predict(imagePath) {
    const model = await loadModel();
    const image = tf.node.decodeImage(fs.readFileSync(imagePath));
    const resizedImage = tf.image.resizeBilinear(image, [224, 224]);
    const normalizedImage = resizedImage.div(tf.scalar(255));
    const batchedImage = normalizedImage.expandDims(0);
    const predictions = await model.predict(batchedImage).data();
    console.log(JSON.stringify(predictions));
}

const imagePath = process.argv[2];
predict(imagePath);
