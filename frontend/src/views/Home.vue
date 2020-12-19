<template>
  <div class="home">
    <div class="back"></div>
    <h1>じゃんけん</h1>
    <fm></fm>
    <div class="room-making">
      <link-button path="/host" class="button-margin">ルーム作成</link-button>
    </div>
  </div>
  
</template>

<script>
import LinkButton from '@/components/Link.vue'
import Form_text from '@/components/Form_text.vue'

export default {
  name: 'Home',
  components: {
    LinkButton,
    "fm": Form_text
  },
}
</script>

<style scoped>
.back {
  background-size: cover;
}
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
}
</style>
