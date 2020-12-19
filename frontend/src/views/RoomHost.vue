<template>
  <div class="user">
    <h1>{{roomname}}</h1>
    <jankenpon ref="jkp"/>
    <button @click="startGame" class="button-margin">じゃんけんスタート！！</button>
    <div class="vs">
      <div class="hands">
        <h2>You</h2>
        <guest-hand :hand="hand" :username="username" :is_win="is_win" class="youHand"/>
        <h1>vs</h1>
      </div>
    </div>
    <eveyone-hand :_data="hands"/>
    <hand-status class="cam" />
  </div>
</template>

<script>
import HandStatus from '../components/HandStatus/HandStatus.vue'
import Jankenpon from '../components/animation/jan_ken_pon.vue'
import GuestHand from '../components/UserHand/GuestHand.vue'
import EveyoneHand from '../components/UserHand/_EveyoneHand.vue'
import io from 'socket.io-client';

export default {
  data () {
    return {
      hand:"0",
      username: "",
      on: false,
      roomname: "shuuuuの部屋",
      is_win: true,
      socket: "",
    }
  },
  components: { 
    HandStatus, 
    GuestHand,
    EveyoneHand,
    Jankenpon
  },
  methods:{
    startGame() {
      this.$refs.jkp.is_start= true
      console.log(this.$refs.jkp.is_start)

    }
  },
  mounted: function(){
    this.username = this.$store.state.username
    this.roomname = this.$store.state.roomname
    const socket = io('/', {
        path: '/ws/socket.io',
        transports:['websocket']
    })
    socket.on('new_hand', msg => console.log(msg))
  },
  watch: {
    hand: function(hand) {
      this.socket.emit('new_hand',{hand})
      console.log("watch")
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
  z-index: 10;
}
</style>
