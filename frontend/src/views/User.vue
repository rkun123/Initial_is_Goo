<template>
  <div class="home">
    <div class="back"></div>
    <div class="container">
      <div class="design">
        <h1>Rock-Paper-Scissors</h1>
        <fm class="fmm1" placeholder="Room ID"></fm>
        <fm class="fmm2" placeholder="User Name"></fm>
        <div class="room-making">
          <button class="button-margin" @click="join">Join</button>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
import Form_text from '@/components/Form_text.vue'

export default {
  name: 'Home',
  components: {
    "fm": Form_text
  },
  methods: {
    join(){
      this.$router.push('/room/1/guest')
    }
  }
}
</script>

<style scoped>
.fmm1 >>> .icon{
  display:none;
}
.fmm2 >>> .icon{
  display:none;
}
.fmm2{
  margin-top: 25px;
}
.back {
  background-size: cover;
}
.button-margin {
  font-size: 20px;
  margin-top: 25px;
  margin-bottom: 25px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-right-radius: 50px;
  border-bottom-left-radius: 50px;
  width: 30%;
  height: 40px;
  max-width: 700px;
  min-width: 200px;
  background-color: rgb(253, 237, 216);
  border: 0.3px solid;
  border: solid;
  border-color: #7575757a;
}
.design{
  backdrop-filter: blur(3px);
  background-color: rgba(253, 245, 236, 0.61);
  border-radius: 5px;
  color: #333;
  line-height: 1.5;
  padding: 1rem 2rem;
  margin: auto;
  border-top-left-radius: 30px;
  border-top-right-radius: 30px;
  border-bottom-right-radius: 30px;
  border-bottom-left-radius: 30px;
  border: solid;
  border: 0.3px solid;
  border: solid;
  border-color: #8b8b8b5e;
  width:100%;
  max-width: 700px;
  min-width: 300px;
}
.container {
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 100%;
}
.button-margin:hover {
  font-weight: bold; /* 太字にする */
  cursor: pointer; /* マウスカーソルを「ポインター」にする */
  background-color: rgb(255, 224, 183);
}
</style>
