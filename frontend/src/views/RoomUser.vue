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

          <guest-hand :hand="getHostHand()" :username="hostname" :is_win="host_win" class="youHand"/>

      </div>
    </div>
    <!--<eveyone-hand :_data="users"/>-->
    <div class="users_container">
    <guest-hand v-for="user in users" :key="user.id" :hand="user.hand" :username="user.name" :is_win="is_win"/>
    </div>
    <hand-status class="cam" />
  </div>
</template>

<script>
import HandStatus from '../components/HandStatus/HandStatus.vue'
import GuestHand from '../components/UserHand/GuestHand.vue'
//import EveyoneHand from '../components/UserHand/_EveyoneHand.vue'

export default {
  data () {
    return {
      hand:0,
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
    //EveyoneHand
  },
  methods: {
    getHostHand() {
      return this.users.find(user => (user.id === this.$store.state.hostid))
    }
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
      console.log(payload)
      if(payload.event =="new_hand"){
        this.users = this.$store.state.users
        if(payload.user_id === this.$store.state.userid){
          console.log('myhand')
          this.hand = payload.hand
        }else if(payload.user_id !== this.$store.state.hostid){
          this.hosthand = payload.hand
          console.log('hosthand')
        }else {
          this.users.map((user) => {
            if(user.id === payload.user_id){
              console.log(user.name, ' hand')
              user.hand = payload.hand
            }
          })
        }

        
      } else if (payload.event=="new_user"){
        const newUser = {
          id:payload.id,
          name:payload.name,
          hand: 0
        }
        if(payload.room_id !== this.$store.state.roomid) return
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
.users_container {
  display: flex;
  flex-wrap: wrap;
}
</style>
