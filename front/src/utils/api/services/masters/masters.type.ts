import type { Tag } from '../tags/tags.type'

export interface Master {
  id: number
  name: string
  phone: string
  image: string
  start_cost: number
  short_description: string | null
  rating: number
  experience: number
  tags: Tag[]
}

export interface MasterParams {
  salon: number
  page?: number
  page_size?: number
}
