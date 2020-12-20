<template>
  <div class="user">
    <div class="container">
      <div class="design">
        <h1>Creat Room</h1>
        <fm1 class="fmm1" placeholder="Room Name"></fm1>
        <fm2 class="fmm2" placeholder="User Neme"></fm2>
        <div class="room-making">
          <button class="button-margin" @click="createRoom">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Form_text from '@/components/Form_text.vue'
import Form_text2 from '@/components/Form_text2.vue'

export default {
  name: 'Host',
  data() {
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
    createRoom(){
      if(this.name=="" || this.room==""){
        console.log(this.name,this.room)
        alert("空欄の箇所があります。")
      } else {
        const data = {
          user_name: this.name,
          room_name: this.room
        }
        fetch('/room', {
          method: "POST",
          body: JSON.stringify(data)
        }).then((res) => {
          return res.json()
        }).then((res) => {
          console.log(res.room)
          this.$store.state.username = res.room.host_user.name
          this.$store.state.roomname = this.room
          this.$store.state.roomid = res.room.id
          this.$store.state.userid = res.room.host_user.id
          this.$router.push("/room/"+res.room.host_user.room_id+"/host")
        }).catch((e) => {
          alert("Fetch failed" + e)
      })
      }
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
.button-margin {
  font-size: 20px;
  margin-top: 25px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-right-radius: 50px;
  border-bottom-left-radius: 50px;
  width: 30%;
  height: 40px;
  max-width: 300px;
  min-width: 100px;
  z-index: 10;
}
.design{
backdrop-filter: blur(3px);
  background-color: rgba(255, 255, 255, 0.61);
  border-radius: 5px;
  color: #333;
  line-height: 1.5;
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
  
}
.container {
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 100%;
}
</style>
