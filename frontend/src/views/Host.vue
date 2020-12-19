<template>
  <div class="user">
    <h1>じゃんけん~ルーム作成~</h1>
    <fm1 class="fmm1" placeholder="Room name"></fm1>
    <fm2 class="fmm2" placeholder="User neme"></fm2>
    <div class="room-making">
      <button class="button-margin" @click="make_room">作成</button>
    </div>
  </div>
</template>

<script>
import Form_text from '@/components/Form_text.vue'

export default {
  name: 'Host',
  components: {
    "fm1": Form_text,
    "fm2": Form_text
  },
  methods: {
    make_room(){
      this.$router.push('/roomhost')
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
  width: 15%;
  height: 40px;
  max-width: 200px;
}

</style>
