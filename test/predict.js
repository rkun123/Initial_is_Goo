function predict(videoElem, model, resultElem) {
    const modelInputWidth = model.input.shape[1];
    const modelInputHeight = model.input.shape[2];

    var canvas = document.createElement('canvas');
    canvas.width = 640;
    canvas.height = 480;
    var ctx = canvas.getContext('2d');

    //draw image to canvas. scale to target dimensions
    ctx.drawImage(videoElem, 0, 0, canvas.width, canvas.height);

    const inputTensor = tf.browser
      .fromPixels(canvas)
      // Resize image to fit neural network input.
      .resizeNearestNeighbor([modelInputWidth, modelInputHeight])
      // Normalize.
      .div(255);

    const prediction = model.predict(
        // Reshape and add one dimension for the pixel color to match CNN input size
        inputTensor.reshape([1, modelInputWidth, modelInputHeight, 3]),
    );
    //console.log(JSON.stringify(prediction))
    const choiceIndex = prediction.argMax(1).dataSync()[0];
    const status = [
        "ぐー",
        "ぱー",
        "ちょき"
    ]
    console.log(prediction.argMax(1).dataSync())
    console.log(status[choiceIndex])

    resultElem.innerHTML = status[choiceIndex]
}