import request from "./request.ts";
import type {PostDetail, PostsListData, PostListItem, ResponseModel} from "../types/posts.ts";

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