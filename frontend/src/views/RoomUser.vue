<template>
  <div class="user">
    <h1>{{roomname}}</h1>
    <div class="vs">
      <div class="hands">
        <h2>You</h2>
        <guest-hand :hand="hand" :username="username" :is_win="is_win" class="youHand"/>
      </div>
      <h1>vs</h1>
      <div class="hands">
        <h2>Host</h2>
        <guest-hand :hand="hosthand" :username="hostname" :is_win="host_win" class="youHand"/>
      </div>
    </div>
    <eveyone-hand :_data="users"/>
    <hand-status class="cam" />
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
      username: "",
      userid: "",
      on: false,
      roomname: "",
      roomid: "",
      is_win: true,
      hostname:"",
      hostid: "",
      hosthand: 0,
      host_win: true,
      users:[]
    }
  },
  components: { 
    HandStatus, 
    GuestHand,
    EveyoneHand
  },
  mounted: function(){
    this.username = this.$store.state.username
    this.hostname = this.$store.state.hostname
    this.hostid = this.$store.state.hostid
    this.roomname = this.$store.state.roomname
    this.users = this.$store.state.users
    this.userid = this.$store.state.userid
    this.roomid = this.$store.state.roomid
    this.websocket = new WebSocket('ws://localhost:8080/websocket')
    this.websocket.onmessage=(event)=>{
      const payload = JSON.parse(event.data)
      if(payload.event =="new_hand"){
        this.users = this.$store.state.users
        
          this.hosthand = payload.hand
        
      } else if (payload.event=="new_user"){
        const newUser = {
          id:payload.id,
          name:payload.name,
          hand: "0"
        }
        this.users.push(newUser)
      } else if (payload.event == "start_game"){
        console.log("start")
      }
    }
  },
  watch: {
    hand: function(hand) {
      const data ={
        event: "new_hand",
        user_id: this.userid,
        room_id: this.roomid,
        hand: hand
      }
      this.websocket.send(JSON.stringify(data)) 
    },
    hosthand: function(hand) {
      this.hosthand = hand
      console.log("guest"+hand)
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
  display: flex;
  margin: auto;
  max-width: 800px;
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
