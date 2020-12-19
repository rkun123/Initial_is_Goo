<template>
  <div class="user">
    <h1>This is an Host page</h1>
    <router-link to="/">Home</router-link><br>
    <HelloWorld msg="じゃんけん~ルーム作成~"/>
    <input v-model="message" placeholder="User name"><br>
    <input v-model="message" placeholder="room name"><br>
    <link-button path="/roomhost">ルーム作成</link-button><br>
  </div>
</template>

<script>
import LinkButton from '@/components/Link.vue'

export default {
  name: 'Host',
  components: {
    LinkButton
  },
}
</script>
