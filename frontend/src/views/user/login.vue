<script setup lang="ts">
import {login} from "../../api/user/user.ts";
import {ref} from "vue";
// 获取路由对象
import {useRouter} from "vue-router";

const username = ref('');
const password = ref('');
const router = useRouter();
// 错误信息
const errorMessage  = ref('');

const loginuser = async () => {
  // 清空错误信息
  errorMessage.value = ''
  // 调用登录接口
  const response = await login(
      username.value,
      password.value
  )
  if (response.data.code === 200){
    console.log('登录成功')
    // 提取Token
  const token = response.data.data.access_token;
  // 保存Token到localStorage,持久化到浏览器
  localStorage.setItem('access_token', token);
  // 跳转到首页
  await router.push('/blog')
  console.log('response==',response)
  }else {
    console.log('登录失败',response.data.message,response.data.code)
    errorMessage.value = response.data.message || '登录失败'
  }

}


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
<!--    登录失败提示-->
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
  </div>
</template>

<style scoped>

</style>