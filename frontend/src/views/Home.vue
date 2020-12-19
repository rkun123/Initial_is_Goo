<template>
  <div class="home">
    <div class="back"></div>
    <div class="container">
      <div class="design">
        <h1>Rock-Paper-Scissors</h1>
        <div class="room-making">
          <link-button path="/room/join" class="button-margin">Join Room</link-button>
        </div>
        <div class="room-making">
          <link-button path="/room/creat" class="button-margin">Creat Room</link-button>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
import LinkButton from '@/components/Link.vue'

export default {
  name: 'Home',
  components: {
    LinkButton,
  },
}
</script>

<style scoped>
.button-margin {
  font-size: 20px;
  margin-top: 50px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-right-radius: 50px;
  border-bottom-left-radius: 50px;
  width: 40%;
  height: 60px;
  max-width: 400px;
  min-width: 200px;
  background-color: rgb(255, 255, 255);
  border: 0.3px solid;
  border: solid;
  border-color: #7575757a;
}
.design{
  backdrop-filter: blur(3px);
  background-color: rgba(255, 255, 255, 0.61);
  border-radius: 5px;
  color: #333;
  line-height: 1.5;
  max-width: 50%;
  min-width: 400px;
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
}
.container {
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 100%;
}


</style>
