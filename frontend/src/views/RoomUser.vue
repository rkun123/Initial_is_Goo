<template>
  <div class="user">
    <h1>{{roomname}}</h1>
    <hand-status class="cam" v-if="on"/>
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
    <h2>みんなの手</h2>
    <div class="everyone">
      <guest-hand :hand="hand" :username="username" class="guestHand"/>
      <guest-hand :hand="hand" :username="username" class="guestHand"/>
      <guest-hand :hand="hand" :username="username" class="guestHand"/>
      <guest-hand :hand="hand" :username="username" class="guestHand"/>
      <guest-hand :hand="hand" :username="username" class="guestHand"/>
      <guest-hand :hand="hand" :username="username" class="guestHand"/>
      <guest-hand :hand="hand" :username="username" class="guestHand"/>
    </div>
  </div>
</template>

<script>
import HandStatus from '../components/HandStatus/HandStatus.vue'
import GuestHand from '../components/UserHand/GuestHand.vue'
export default {
  data () {
    return {
      hand:"0",
      username: "shuuuu",
      on: false,
      roomname: "shuuuuの部屋"
    }
  },
  components: { 
    HandStatus, 
    GuestHand 
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

.everyone {
  display: flex;
  flex-wrap :wrap;
}
.everyone .guestHand {
  size: 80%;
  margin: 5px;
}
</style>
