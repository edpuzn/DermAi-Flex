<template>
  <div class="flex items-center justify-between p-3 bg-white rounded-lg border border-gray-100 shadow-sm group relative overflow-hidden transition-all hover:border-indigo-100 hover:shadow-md">
    <div v-if="previewUrl && type === 'image'" class="h-12 w-12 rounded-md overflow-hidden bg-gray-50 border border-gray-200 flex-shrink-0">
      <img :src="previewUrl" class="h-full w-full object-cover" alt="Preview" />
    </div>
    
    <div v-else class="h-12 w-12 rounded-md bg-indigo-50 border border-indigo-100 flex items-center justify-center flex-shrink-0 text-indigo-600">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
    </div>

    <div class="ml-3 flex-1 min-w-0">
      <p class="text-sm font-semibold text-gray-900 truncate">{{ file.name }}</p>
      <p class="text-xs text-gray-500 mt-0.5">{{ formattedSize }}</p>
    </div>

    <button @click.stop="$emit('remove')" class="ml-2 p-1.5 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-md transition-colors opacity-0 group-hover:opacity-100 focus:opacity-100 focus:outline-none" :title="$t('action.remove')">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
    </button>
  </div>
</template>

<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  file: {
    type: File,
    required: true
  },
  type: {
    type: String,
    required: true,
    validator: (v) => ['image', 'pdf'].includes(v)
  }
})

const emit = defineEmits(['remove'])

const previewUrl = ref(null)

const formattedSize = computed(() => {
  if (!props.file) return ''
  const bytes = props.file.size
  if (bytes === 0) return '0 Bytes'
  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i]
})

onMounted(() => {
  if (props.type === 'image' && props.file) {
    previewUrl.value = URL.createObjectURL(props.file)
  }
})

onUnmounted(() => {
  if (previewUrl.value) {
    URL.revokeObjectURL(previewUrl.value)
  }
})
</script>
