<template>
  <div class="home">
    <div class="back"></div>
    <div class="container">
      <div class="design">
        <h1>Rock-Paper-Scissors</h1>
        <fm1 class="fmm1" placeholder="Room ID"></fm1>
        <fm2 class="fmm2" placeholder="User Name"></fm2>
        <div class="room-making">
          <button class="button-margin" @click="join">Join</button>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
import Form_text from '@/components/Form_text.vue'
import Form_text2 from '@/components/Form_text2.vue'

export default {
  name: 'Home',
  data () {
    return {
      name: "",
      room: ""
    }
  },
  components: {
    "fm1": Form_text,
    "fm2": Form_text2
  },
  methods: {
    join(){
      if(this.name=="" || this.room==""){
        console.log(this.name,this.room)
        alert("空欄の箇所があります。")
      } else {
        const data = {
          user_name: this.name
        }
        fetch('/room/'+this.room, {
          method: "POST",
          body: JSON.stringify(data)
        }).then((res) => {
          return res.json()
        }).then((res) => {
          this.$store.state.users = res.room.users.map((user) => {
            user.hand = 0
            return user
          })//配列に初期値グーを挿入している
          console.log(res,"dfgdg")
          this.$store.state.username = this.name
          this.$store.state.hostname = res.room.host_user.name
          this.$store.state.hostid = res.room.host_user.id
          this.$store.state.roomname = res.room.name
          this.$store.state.roomid = this.room
          this.$store.state.userid = res.user.id
          this.$router.push("/room/"+res.room.host_user.room_id+"/guest")
        }).catch((e) => {
          console.log(e)
          alert("Fetch failed" + e)
        })
      }
    }
  },
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
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-right-radius: 50px;
  border-bottom-left-radius: 50px;
  width: 30%;
  height: 40px;
  max-width: 700px;
  min-width: 200px;
}
.design{
  backdrop-filter: blur(3px);
  background-color: rgba(255, 255, 255, 0.61);
  border-radius: 5px;
  color: #333;
  line-height: 1.5;
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
</style>
