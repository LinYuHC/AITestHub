<script setup lang="ts">

// ==================================================
// Vue
// ==================================================

// ref：定义响应式数据
import { ref } from 'vue'


// ==================================================
// 图片上传 API
// ==================================================

// 复用你已经写好的图片上传接口
import { uploadImage } from '../api/blog/posts.ts'


// ==================================================
// 定义 v-model
// ==================================================
//
// 父组件可以这样使用：
//
// <CoverImageUploader
//   v-model="createPostData.cover_image"
// />
//
// v-model 的值就是：
// 图片 URL
//
// 例如：
// /static/images/abc123.jpg
// ==================================================

const coverImage = defineModel<string>({
  default: ''
})


// ==================================================
// 文件选择 input
// ==================================================
//
// 用户点击上传区域以后，
// 实际上还是由 input[type=file] 选择文件。
//
// 这里只是把 input 隐藏起来，
// 用户看到的是我们自己设计的上传区域。
// ==================================================

const fileInput = ref<HTMLInputElement | null>(null)


// ==================================================
// 上传状态
// ==================================================

const uploading = ref(false)


// ==================================================
// 错误信息
// ==================================================

const errorMessage = ref('')


// ==================================================
// 打开文件选择器
// ==================================================

const openFileSelector = () => {

  fileInput.value?.click()

}


// ==================================================
// 校验图片
// ==================================================

const validateImage = (file: File) => {

  // ----------------------------------------------
  // 1. 判断是不是图片
  // ----------------------------------------------

  if (!file.type.startsWith('image/')) {

    errorMessage.value = '请选择图片文件'

    return false

  }


  // ----------------------------------------------
  // 2. 限制图片大小
  //
  // 这里暂时限制 5MB。
  // ----------------------------------------------

  const maxSize = 5 * 1024 * 1024

  if (file.size > maxSize) {

    errorMessage.value = '图片不能超过 5MB'

    return false

  }


  return true

}


// ==================================================
// 上传图片
// ==================================================

const handleUpload = async (file: File) => {

  // 每次上传前清除旧错误
  errorMessage.value = ''


  // 校验图片
  if (!validateImage(file)) {
    return
  }


  // 设置上传状态
  uploading.value = true


  try {

    // ----------------------------------------------
    // 调用后端图片上传接口
    // ----------------------------------------------

    const response = await uploadImage(file)


    console.log(
      '封面图上传响应：',
      response
    )


    // ----------------------------------------------
    // 获取后端返回的图片 URL
    // ----------------------------------------------
    //
    // 假设后端返回：
    //
    // {
    //   code: 200,
    //   data: {
    //     url: "/static/abc.jpg"
    //   }
    // }
    //
    // 那么这里得到：
    //
    // /static/abc.jpg
    // ----------------------------------------------

    const imageUrl =
      response.data.data.url


    // ----------------------------------------------
    // 将图片 URL 写入 v-model
    //
    // 父组件中的：
    //
    // createPostData.cover_image
    //
    // 会自动同步成这个 URL。
    // ----------------------------------------------

    coverImage.value = imageUrl


    console.log(
      '封面图 URL：',
      coverImage.value
    )

  } catch (error) {

    console.error(
      '封面图上传失败：',
      error
    )

    errorMessage.value =
      '图片上传失败，请稍后再试'

  } finally {

    // 上传结束
    uploading.value = false

  }

}


// ==================================================
// 处理文件选择
// ==================================================

const handleFileChange = (
  event: Event
) => {

  // 获取 input 元素
  const input =
    event.target as HTMLInputElement


  // 没有选择文件
  if (!input.files || input.files.length === 0) {
    return
  }


  // 获取用户选择的第一张图片
  const file = input.files[0]


  // 上传
  handleUpload(file)

  // 清空 input
  //
  // 这样用户选择同一张图片时，
  // change 事件也可以再次触发。
  input.value = ''

}


// ==================================================
// 处理拖拽
// ==================================================

const isDragging = ref(false)


// 用户把图片拖进区域
const handleDragOver = (
  event: DragEvent
) => {

  // 阻止浏览器默认打开图片
  event.preventDefault()

  isDragging.value = true

}


// 用户拖出区域
const handleDragLeave = (
  event: DragEvent
) => {

  event.preventDefault()

  isDragging.value = false

}


// 用户释放图片
const handleDrop = (
  event: DragEvent
) => {

  // 阻止浏览器默认打开图片
  event.preventDefault()

  isDragging.value = false


  // 获取拖拽的数据
  const files = event.dataTransfer?.files


  if (!files || files.length === 0) {
    return
  }


  // 我们只需要第一张
  const file = files[0]


  // 上传
  handleUpload(file)

}


// ==================================================
// 处理 Ctrl + V 粘贴图片
// ==================================================

const handlePaste = (
  event: ClipboardEvent
) => {

  // 获取剪贴板数据
  const items = event.clipboardData?.items


  if (!items) {
    return
  }


  // 遍历剪贴板内容
  for (const item of items) {

    // 判断是不是图片
    if (item.type.startsWith('image/')) {

      // 从剪贴板获取 File
      const file = item.getAsFile()


      if (!file) {
        continue
      }


      // 阻止浏览器默认粘贴行为
      event.preventDefault()


      // 上传图片
      handleUpload(file)


      // 找到图片后就可以结束循环
      break

    }

  }

}


// ==================================================
// 删除封面图
// ==================================================

const removeImage = () => {

  coverImage.value = ''

  errorMessage.value = ''

}

</script>


<template>

  <div class="cover-uploader">

    <!--
      隐藏的文件选择框

      accept="image/*"
      表示只允许选择图片。
    -->
    <input
      ref="fileInput"
      type="file"
      accept="image/*"
      class="hidden-file-input"
      @change="handleFileChange"
    />


    <!-- ==================================================
         已经上传封面
         ================================================== -->

    <div
      v-if="coverImage"
      class="preview-container"
    >

      <!-- 图片预览 -->
      <img
        :src="coverImage"
        alt="文章封面"
        class="cover-preview"
      />


      <!-- 操作按钮 -->
      <div class="preview-actions">

        <button
          type="button"
          class="action-button"
          @click="openFileSelector"
        >
          重新上传
        </button>


        <button
          type="button"
          class="action-button danger"
          @click="removeImage"
        >
          删除
        </button>

      </div>

    </div>


    <!-- ==================================================
         还没有封面
         ================================================== -->


    <div
      v-else
      class="upload-area"
      :class="{ dragging: isDragging }"
      @click="openFileSelector"
      @dragover="handleDragOver"
      @dragleave="handleDragLeave"
      @drop="handleDrop"
      @paste="handlePaste"
      >
      <!--
        点击上传
        拖拽上传
        粘贴上传
      -->


      <!-- 上传状态 -->
      <template v-if="uploading">

        <div class="upload-icon">
          ⏳
        </div>

        <div class="upload-title">
          正在上传...
        </div>

      </template>


      <!-- 正常状态 -->
      <template v-else>

        <div class="upload-icon">
          🖼️
        </div>

        <div class="upload-title">
          上传文章封面
        </div>

        <div class="upload-description">
          点击选择、拖拽图片，或者 Ctrl + V 粘贴图片
        </div>

      </template>

    </div>


    <!-- 错误信息 -->
    <p
      v-if="errorMessage"
      class="error-message"
    >
      {{ errorMessage }}
    </p>

  </div>

</template>


<style scoped>

/* ==================================================
 * 隐藏原生文件选择框
 * ================================================== */

.hidden-file-input {
  display: none;
}


/* ==================================================
 * 上传区域
 * ================================================== */

.upload-area {
  min-height: 220px;

  display: flex;

  flex-direction: column;

  align-items: center;

  justify-content: center;

  padding: 30px;

  border: 2px dashed #334155;

  border-radius: 12px;

  background: #0b1118;

  cursor: pointer;

  transition:
    border-color 0.2s ease,
    background-color 0.2s ease,
    box-shadow 0.2s ease;
}


/* ==================================================
 * 鼠标悬浮
 * ================================================== */

.upload-area:hover {
  border-color: #00ff88;

  background: rgba(0, 255, 136, 0.03);

  box-shadow:
    0 0 20px rgba(0, 255, 136, 0.08);
}


/* ==================================================
 * 正在拖拽
 * ================================================== */

.upload-area.dragging {
  border-color: #00ff88;

  background: rgba(0, 255, 136, 0.08);

  box-shadow:
    0 0 25px rgba(0, 255, 136, 0.15);
}


/* ==================================================
 * 上传图标
 * ================================================== */

.upload-icon {
  margin-bottom: 14px;

  font-size: 40px;
}


/* ==================================================
 * 上传标题
 * ================================================== */

.upload-title {
  color: #00ff88;

  font-size: 16px;

  font-weight: 700;
}


/* ==================================================
 * 上传说明
 * ================================================== */

.upload-description {
  margin-top: 10px;

  color: #6b8f7a;

  font-size: 12px;

  text-align: center;
}


/* ==================================================
 * 预览区域
 * ================================================== */

.preview-container {
  padding: 14px;

  border: 1px solid rgba(0, 255, 136, 0.2);

  border-radius: 12px;

  background: #0b1118;
}


/* ==================================================
 * 封面预览
 * ================================================== */

.cover-preview {
  display: block;

  width: 100%;

  max-height: 360px;

  object-fit: cover;

  border-radius: 8px;
}


/* ==================================================
 * 预览操作
 * ================================================== */

.preview-actions {
  display: flex;

  justify-content: center;

  gap: 12px;

  margin-top: 12px;
}


/* ==================================================
 * 操作按钮
 * ================================================== */

.action-button {
  padding: 7px 14px;

  border: 1px solid rgba(0, 255, 136, 0.3);

  border-radius: 5px;

  background: transparent;

  color: #00ff88;

  font-family: inherit;

  font-size: 12px;

  cursor: pointer;
}


/* ==================================================
 * 删除按钮
 * ================================================== */

.action-button.danger {
  border-color: rgba(255, 80, 80, 0.3);

  color: #ff6b6b;
}


/* ==================================================
 * 错误提示
 * ================================================== */

.error-message {
  margin-top: 10px;

  color: #ff6b6b;

  font-size: 12px;

}

</style>