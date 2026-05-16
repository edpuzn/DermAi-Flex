import { defineStore } from 'pinia'
import { analysisService } from '../services/api'

export const useAnalysisStore = defineStore('analysis', {
  state: () => ({
    imageFile: null,
    pdfFile: null,
    combinedFiles: [],
    isAnalyzing: false,
    currentStep: '', // 'uploading', 'analyzing', 'extracting', 'synthesizing'
    analysisResult: null,
    error: null,
    history: []
  }),
  
  actions: {
    setImageFile(file) {
      this.imageFile = file
    },
    setPdfFile(file) {
      this.pdfFile = file
    },
    setCombinedFiles(files) {
      this.combinedFiles = files
    },
    clearFiles() {
      this.imageFile = null
      this.pdfFile = null
      this.combinedFiles = []
      this.currentStep = ''
    },
    async runAnalysis() {
      this.isAnalyzing = true
      this.error = null
      this.currentStep = 'uploading'
      
      const timeout = setTimeout(() => {
        if (this.isAnalyzing) {
          this.error = "Analysis is taking longer than expected. Please check your connection."
          this.isAnalyzing = false
        }
      }, 60000) // 60s timeout

      try {
        const img = this.imageFile || this.combinedFiles.find(f => f.type.startsWith('image/'))
        const pdf = this.pdfFile || this.combinedFiles.find(f => f.type === 'application/pdf')
        
        this.currentStep = 'analyzing'
        const result = await analysisService.analyze(img, pdf)
        
        this.currentStep = 'finishing'
        this.analysisResult = result
        
        this.history.unshift({
          id: Date.now(),
          timestamp: new Date(),
          result: result
        })
        
        clearTimeout(timeout)
      } catch (err) {
        clearTimeout(timeout)
        this.error = err.response?.data?.detail || err.message || "An unexpected error occurred during analysis."
      } finally {
        this.isAnalyzing = false
        this.currentStep = ''
      }
    }
  }
})


