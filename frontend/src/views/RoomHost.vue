<template>
  <div class="user">
    <h1>{{roomname}}</h1>
    <button @click="startGame" class="button-margin">じゃんけんスタート！！</button>
    <div class="vs">
      <div class="hands">
        <h2>You</h2>
        <guest-hand :hand="hand" :username="username" :is_win="is_win" class="youHand"/>
        <h1>vs</h1>
      </div>
    </div>
    <eveyone-hand :_data="hands"/>
    <hand-status class="cam" v-if="on"/>
  </div>
</template>

<script>
import HandStatus from '../components/HandStatus/HandStatus.vue'
import GuestHand from '../components/UserHand/GuestHand.vue'
import EveyoneHand from '../components/UserHand/_EveyoneHand.vue'

export default {
  data () {
    return {
      hand:"0",
      username: "shuuuu",
      on: false,
      roomname: "shuuuuの部屋",
      is_win: true
    }
  },
  components: { 
    HandStatus, 
    GuestHand,
    EveyoneHand 
  },
  methods: {
    startGame() {

    }
  }
}
</script>

<style scoped>
.cam {
  position: fixed;
  bottom: 10px;
  right: 10px;
}
.user h1{
  font-size: 50px;
}
.user h2 {
  font-size: 36px;
}
.vs {
  margin: auto;
}
.vs .youHand {
  margin: auto;
}
.vs h1 {
  font-size: 60px;
}
.button-margin {
  font-size: 20px;
  margin-top: 30px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-right-radius: 50px;
  border-bottom-left-radius: 50px;
  width: 40%;
  height: 60px;
  max-width: 400px;
  background-color: whitesmoke;
  cursor: pointer;
}
</style>
