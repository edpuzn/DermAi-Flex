import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export const analysisService = {
  async analyze(imageFile, pdfFile, metadata = {}) {
    const formData = new FormData()
    if (imageFile) formData.append('image', imageFile)
    if (pdfFile) formData.append('pdf', pdfFile)
    formData.append('metadata', JSON.stringify(metadata))

    const response = await apiClient.post('/analysis/analyze', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    return response.data
  },
}

export default apiClient
