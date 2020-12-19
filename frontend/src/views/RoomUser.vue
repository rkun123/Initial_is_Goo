<template>
  <div class="user">
    <h1>{{roomname}}</h1>
    <div class="vs">
      <div class="hands">
        <h2>You</h2>
        <guest-hand :hand="hand" :username="username" class="youHand"/>
      </div>
      <h1>vs</h1>
      <div class="hands">
        <h2>Host</h2>
        <guest-hand :hand="hand" :username="username" class="youHand"/>
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
    }
  },
  components: { 
    HandStatus, 
    GuestHand,
    EveyoneHand 
  },
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
  display: flex;
  margin: auto;
}
.vs h1 {
  vertical-align: middle;
  font-size: 100px;
  margin: auto;
}
.vs h2{
  font-size: 40px;
}
.vs .youHand {
  margin: auto;
}
.vs .hands{
  text-align: center;
  width:30%;
}
</style>
