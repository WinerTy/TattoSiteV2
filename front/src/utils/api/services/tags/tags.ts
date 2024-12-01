import type { AxiosInstance, AxiosPromise } from 'axios'
import type { ApiResponse } from '../../base/base.type'
import type { Tag, TagParams } from './tags.type'

export default (instance: AxiosInstance) => ({
  getTags(params: TagParams): AxiosPromise<ApiResponse<Tag>> {
    return instance.get('/tags/', { params })
  },
})
