import request from "./request.ts";
import type {PostListItem, ResponseModel} from "../types/post.ts";

export function getPostsList(
  title?: string,
  page = 1,
  pageSize = 10
) {
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