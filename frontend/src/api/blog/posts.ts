import request from "../request.ts";
import type {PostDetail, PostsListData, ResponseModel, CreatePostRequest} from "../../types/posts.ts";

export function getPostsList(
  title?: string,
  page = 1,
  pageSize = 1
) {
  //   调用博客列表接口
  return request.get<ResponseModel<PostsListData>>(
    '/api/v1/posts/list',
    {
      params: {
        title,
        page,
        page_size: pageSize
      }
    }
  )
}

export function getPostDetail(posts_id: number) {
  //   调用博客详情接口
  return request.get<ResponseModel<PostDetail>>(
    `/api/v1/posts/details`,
      {
        params: {
            posts_id
        }
    }
  )
}

export function createPost(data: CreatePostRequest) {
  //   调用创建博客接口
  return request.post<ResponseModel<null>>(
    '/api/v1/posts/create',
    data
  )
}

export function uploadImage(file: File) {
  const formData = new FormData()

  formData.append('file', file)

  return request.post(
    '/api/v1/upload/',
    formData
  )
}
