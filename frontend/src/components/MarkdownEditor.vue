<script setup lang="ts">

// ==================================================
// Vue
// ==================================================

import { ref } from 'vue'


// ==================================================
// Markdown 编辑器
// ==================================================

import { MdEditor } from 'md-editor-v3'

// 编辑器官方样式必须引入
import 'md-editor-v3/lib/style.css'


// ==================================================
// 图片上传接口
// ==================================================

import { uploadImage } from '../api/blog/posts.ts'


// ==================================================
// 父组件传入的 Markdown 数据
// ==================================================
//
// 父组件：
//
// <MarkdownEditor
//   v-model="createPostData.content"
// />
//
// defineModel 会自动帮我们处理：
//
// props
// +
// emit
//
// 所以这里不用自己写 defineProps / defineEmits。
// ==================================================

const content = defineModel<string>({
  default: ''
})


// ==================================================
// 图片上传
// ==================================================

const onUploadImg = async (
  files: File[],
  callback: (urls: string[]) => void
) => {

  try {

    /*
     * 同时上传多张图片
     */
    const responses = await Promise.all(
      files.map((file) => uploadImage(file))
    )


    /*
     * 提取后端返回的 URL
     *
     * 假设返回：
     *
     * {
     *   code: 200,
     *   data: {
     *     url: '/static/xxx.png'
     *   }
     * }
     */
    const urls = responses.map(
      (response) => response.data.data.url
    )


    console.log(
      '图片上传成功：',
      urls
    )


    /*
     * 把 URL 交给编辑器。
     *
     * 编辑器会自动把 URL 转成 Markdown 图片：
     *
     * ![图片](URL)
     */
    callback(urls)

  } catch (error) {

    console.error(
      '图片上传失败：',
      error
    )

  }

}

</script>


<template>

  <!--
    这里直接使用 defineModel 的 content。

    这样：

    父组件：
    createPostData.content

            ↕️

    MarkdownEditor

            ↕️

    MdEditor
  -->

<MdEditor
    v-model="content"
    :preview="true"
    :height="600"
    @onUploadImg="onUploadImg"
    preview-theme="github"
  />

    <!-- 开启右侧 Markdown 预览 -->


    <!-- 编辑器高度 -->


    <!-- 图片上传 -->


    <!-- Markdown 预览主题 -->



</template>