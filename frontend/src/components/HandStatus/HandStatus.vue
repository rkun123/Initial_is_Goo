<template>
  <div>
    <video id="webcam" autoplay width="640" height="480"></video>
    <button id="enableCamButton">Enable Webcam</button>
    <h1 id="resultElem"></h1>
  </div>
</template>

<script>
import {predict} from '@/plugins/predict.js'
import * as tf from '@tensorflow/tfjs';
export default {
  name: "HandStatus",
  data() {
    return {
      video:"",
      resultElem:""
    }
  },
  methods: {
    prepareModel() {
      const self = this
      tf.loadLayersModel('/model/rock_paper_scissors_mobilenet_v2/model.json').then(handleModel).catch(handleError)
      function handleModel(model) {
        console.info('Loaded model')
        console.log(model)
        setInterval(predict, 500, self.video, model, self.resultElem)
        //predict(video, model)    
      }
      function handleError(error) 
      {
        console.error(error)
      }
    },
    enableCam(event) {
      console.log(event)
        navigator.mediaDevices.getUserMedia({video: true, audio: false}).then((localMediaStream) => 
        {
          console.log(localMediaStream)
          this.video.srcObject = localMediaStream;
          this.video.onloadedmetadata = (e) => 
          {
            console.log('Video loaded')
            console.log(e)
            this.prepareModel()
          }
        }).catch((e) => 
        {
          console.error(e)
        })
    },
  },
  mounted: function(){
    this.video = document.getElementById('webcam');
    const enableWebCamButton = document.getElementById('enableCamButton')
    this.resultElem = document.getElementById('resultElem')
    enableWebCamButton.addEventListener('click', this.enableCam());
  }
}
</script>
