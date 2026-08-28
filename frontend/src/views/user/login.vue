<script setup lang="ts">
import {login} from "../../api/user/user.ts";
import {ref, onMounted} from "vue";

const username = ref('');
const password = ref('');

const loginuser = async () => {
  // 调用登录接口
  const response = await login(
      username.value,
      password.value
  )
  // 提取Token
  const token = response.data.data.access_token;
  // 保存Token到localStorage,持久化到浏览器
  localStorage.setItem('access_token', token);

  console.log(response)
  console.log('账号密码===',username.value,password.value)
  console.log('Token===',response.data.data.access_token)
}

// onMounted(() => {
//   loginuser()
// })

</script>

<template>
  <div>
    <h3>login</h3>
    <form @submit.prevent="loginuser">
<!--      @submit.prevent="loginuser" 表示使用表单提交，当点击button按钮登录后，会自动调用loginuser方法-->
      <input type="text" placeholder="用户名" v-model="username" />
      <input type="password" placeholder="密码" v-model="password" />
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<style scoped>

</style>