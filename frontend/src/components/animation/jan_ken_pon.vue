<template>
  <div>
    <h1 class="ml4" v-if="is_start">
      <span class="letters letters-1">じゃん</span>
      <span class="letters letters-2">けん</span>
      <span class="letters letters-3">ぽん！</span>
    </h1>
    <button @click="is_start=!is_start">go</button>
  </div>
</template>

<script>
import anime from 'animejs'
export default {
  data () {
    return {
      is_start: false
    }
  },
  methods: {
    startCall() {
      var ml4 = {};
      ml4.opacityIn = [0,1];
      ml4.scaleIn = [0.2, 1];
      ml4.scaleOut = 3;
      ml4.durationIn = 800;
      ml4.durationOut = 600;
      ml4.delay = 500;

    anime.timeline({loop: false})
      .add({
        targets: '.ml4 .letters-1',
        opacity: ml4.opacityIn,
        scale: ml4.scaleIn,
        duration: ml4.durationIn
      }).add({
        targets: '.ml4 .letters-1',
        opacity: 0,
        scale: ml4.scaleOut,
        duration: ml4.durationOut,
        easing: "easeInExpo",
        delay: ml4.delay
      }).add({
        targets: '.ml4 .letters-2',
        opacity: ml4.opacityIn,
        scale: ml4.scaleIn,
        duration: ml4.durationIn
      }).add({
        targets: '.ml4 .letters-2',
        opacity: 0,
        scale: ml4.scaleOut,
        duration: ml4.durationOut,
        easing: "easeInExpo",
        delay: ml4.delay
      }).add({
        targets: '.ml4 .letters-3',
        opacity: ml4.opacityIn,
        scale: ml4.scaleIn,
        duration: ml4.durationIn
      }).add({
        targets: '.ml4 .letters-3',
        opacity: 0,
        scale: ml4.scaleOut,
        duration: ml4.durationOut,
        easing: "easeInExpo",
        delay: ml4.delay
      }).add({
        targets: '.ml4',
        opacity: 0,
        duration: 500,
        delay: 500
      });
    }
  },
  watch: {
    is_start: function() {
      if(this.is_start) {
      this.startCall()
      }
    }
  }
}
</script>

<style scoped>
.ml4 {
  position: relative;
  font-weight: 900;
  font-size: 4.5em;
  z-index: 20;
}
.ml4 .letters {
  position: absolute;
  margin: auto;
  left: 0;
  top: 0.3em;
  right: 0;
  opacity: 0; 
  z-index: 20;
}
</style>
