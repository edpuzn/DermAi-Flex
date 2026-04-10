<template>
  <div 
    class="relative flex flex-col group rounded-xl p-6 transition-all duration-300 border bg-white h-full"
    :class="[
      highlight ? 'border-2 border-indigo-200 shadow-xl lg:scale-[1.02] bg-indigo-50/10' : 'border-gray-200 shadow-sm hover:shadow-md hover:border-indigo-100',
      isDragging ? 'border-indigo-500 bg-indigo-50/50' : ''
    ]"
    @dragenter.prevent="isDragging = true"
    @dragover.prevent="isDragging = true"
    @dragleave.prevent="isDragging = false"
    @drop.prevent="handleDrop"
  >
    <div class="flex items-center justify-between mb-2">
      <div class="flex items-center space-x-3">
        <div :class="iconContainerClass" class="w-10 h-10 rounded-lg flex items-center justify-center">
          <slot name="icon"></slot>
        </div>
        <h3 class="text-lg font-semibold text-gray-900">{{ title }}</h3>
      </div>
      <span v-if="highlight" class="inline-flex items-center px-2 py-1 rounded-full text-[10px] uppercase tracking-wider font-bold bg-green-100 text-green-700 border border-green-200">
        AI Multimodal
      </span>
    </div>
    
    <p class="text-sm text-gray-500 mb-6 flex-grow">{{ description }}</p>

    <!-- Upload Area -->
    <div v-if="!hasFiles" class="mt-auto flex flex-col items-center justify-center border-2 border-dashed rounded-xl p-6 transition-colors"
         :class="[
           isDragging ? 'border-indigo-500 bg-indigo-50' : 'border-gray-300 group-hover:border-indigo-300',
           highlight ? 'bg-white/50' : 'bg-gray-50'
         ]"
    >
      <input 
        type="file" 
        :accept="accept" 
        :multiple="type === 'combined'"
        class="hidden" 
        ref="fileInput" 
        @change="handleFileSelect" 
      />
      
      <button 
        type="button"
        @click="$refs.fileInput.click()"
        class="flex flex-col items-center focus:outline-none w-full"
      >
        <svg class="w-8 h-8 text-indigo-400 mb-3 group-hover:text-indigo-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
        <span class="text-sm font-semibold text-indigo-600 hover:text-indigo-800 transition-colors">{{ $t('action.browse') }}</span>
        <span class="text-xs text-gray-500 mt-1 font-medium">{{ $t('action.dragDrop') }}</span>
        <span class="text-[10px] text-gray-400 mt-2 text-center uppercase tracking-wide">{{ acceptLabel }}</span>
      </button>
    </div>

    <!-- Preview Area -->
    <div v-else class="mt-auto flex flex-col gap-3">
      <template v-if="type === 'image' || type === 'pdf'">
        <FilePreview 
          :file="file" 
          :type="type" 
          @remove="$emit('remove')" 
        />
      </template>
      <template v-else>
        <div class="space-y-2">
          <FilePreview 
            v-for="(f, index) in files" 
            :key="f.name + index"
            :file="f" 
            :type="getFileType(f)" 
            @remove="$emit('remove', index)" 
          />
        </div>
        <button 
          v-if="files.length < 2"
          @click="$refs.fileInput.click()"
          class="w-full py-2 px-4 border border-dashed border-gray-300 rounded-lg text-sm font-medium text-gray-600 hover:text-indigo-600 hover:border-indigo-400 transition-colors bg-white hover:bg-indigo-50"
        >
          <span class="flex items-center justify-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
            {{ $t('action.addAnother') }}
          </span>
        </button>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import FilePreview from './FilePreview.vue'

const { t } = useI18n()

const props = defineProps({
  type: {
    type: String,
    required: true,
    validator: v => ['image', 'pdf', 'combined'].includes(v)
  },
  title: String,
  description: String,
  accept: String,
  highlight: {
    type: Boolean,
    default: false
  },
  file: {
    type: File,
    default: null
  },
  files: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['file-selected', 'remove', 'error'])
const fileInput = ref(null)
const isDragging = ref(false)

const hasFiles = computed(() => {
  if (props.type === 'combined') {
    return props.files && props.files.length > 0
  }
  return props.file !== null
})

const iconContainerClass = computed(() => {
  if (props.type === 'image') return 'bg-blue-50 text-blue-600'
  if (props.type === 'pdf') return 'bg-orange-50 text-orange-600'
  return 'bg-gradient-to-br from-indigo-500 to-purple-600 text-white shadow-inner'
})

const acceptLabel = computed(() => {
  if (props.type === 'image') return t('action.imgAccept')
  if (props.type === 'pdf') return t('action.pdfAccept')
  return t('action.multiAccept')
})

const getFileType = (file) => {
  if (file.type.startsWith('image/')) return 'image'
  if (file.type === 'application/pdf') return 'pdf'
  return 'unknown'
}

const validateFiles = (fileList) => {
  const validFiles = []
  Array.from(fileList).forEach(f => {
    if (props.type === 'image' && !f.type.startsWith('image/')) {
      emit('error', t('action.errImg'))
    } else if (props.type === 'pdf' && f.type !== 'application/pdf') {
      emit('error', t('action.errPdf'))
    } else {
      validFiles.push(f)
    }
  })
  return validFiles
}

const handleFileSelect = (e) => {
  const selectedFiles = validateFiles(e.target.files)
  if (selectedFiles.length > 0) {
    if (props.type === 'combined') {
      emit('file-selected', selectedFiles)
    } else {
      emit('file-selected', selectedFiles[0])
    }
  }
  if (fileInput.value) fileInput.value.value = ''
}

const handleDrop = (e) => {
  isDragging.value = false
  const droppedFiles = validateFiles(e.dataTransfer.files)
  if (droppedFiles.length > 0) {
    if (props.type === 'combined') {
      emit('file-selected', droppedFiles)
    } else {
      emit('file-selected', droppedFiles[0])
    }
  }
}
</script>
