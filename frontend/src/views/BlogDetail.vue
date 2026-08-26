<script setup lang="ts">
// ref：创建响应式数据
// onMounted：页面加载完成后执行代码
import { ref, onMounted } from 'vue'
// useRoute：获取当前路由信息
import { useRoute } from  'vue-router'
// 导入接口调用
import { getPostDetail } from '../api/posts'
// 导入文章详情类型
import type{ PostDetail } from '../types/posts'

// ------------------------------------
// 获取当前路由对象
// ------------------------------------
//
// 如果当前地址是：
// /blog/2
//
// 那么 route.params.id 就是：
// "2"
// ------------------------------------
const route = useRoute()

// ------------------------------------
// 定义文章详情数据
//
// 页面刚打开的时候还没有文章数据
// 所以先使用 null
// ------------------------------------
const post = ref<PostDetail | null>(null)

// 请求文章详情
const loadPostDateil = async () => {
  // 从 URL 中获取 id
  //注意：Vue Router 的 params 默认是 string,即：route.params.id = "2",但我们的后端方法需要：number,所以要进行 Number 转换。
  const id = Number(route.params.id)

  //   调用获取文章详情的方法
  const response = await getPostDetail(id)
  // 把后端返回的数据保存到响应式变量
  post.value = response.data.data
  console.log('文章详情：', response.data.data)

}
// 页面挂载完成以后请求文章详情
  onMounted(()=>{
    loadPostDateil()
  })
</script>

<template>
  <div>
    <p v-if="!post">
      正在加载文章...
    </p>
    <div v-else>
      <p>{{ post.title }}</p>
      <p>{{ post.summary }}</p>
      <p>{{ post.content }}</p>
      <p>{{ post.cover_image }}</p>
    </div>
  </div>

</template>

<style scoped>

</style>
