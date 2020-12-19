<template>
  <div class="jankenpon" v-show="isOpen" @click="close">
    <h1 class="ml4">
      <span class="letters letters-1">じゃん</span>
      <span class="letters letters-2">けん</span>
      <span class="letters letters-3">ぽん!</span>
    </h1>
  </div>
</template>

<script>
import anime from 'animejs'
export default {
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
    async startCall() {
      console.log(this.isOpen)
      if(this.isOpen) {
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
          }
        )
      }
    },
    close() {
      this.isOpen = false
    },
    openAnime() {
      this.startCall().await(()=>{console.log("then")})
    }
  },
  watch:{
    isOpen: function(value) {
      this.isOpen = value
      this.openAnime()
    }
  }
}
</script>

<style scoped>
.jankenpon {
  width:100%;
	height:120%;
	position:fixed;
	top:0;
	left:0;
  background-color: #000000af;
  backdrop-filter: blur(15px);
}
.ml4 {
  position: relative;
  font-weight: 900;
  font-size: 15vw;
}
.ml4 .letters {
  position: absolute;
  margin: auto;
  left: 0;
  right: 0;
  opacity: 0;
  color: white;
}

</style>
