<template>
    <div class="min-h-screen bg-gray-100 p-8">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-2xl font-bold mb-6">Tasks</h2>
        <ul class="space-y-4">
          <li
            v-for="task in tasks"
            :key="task.id"
            class="bg-white p-4 rounded-lg shadow-md"
          >
            <div class="flex justify-between items-center">
              <div>
                <h3 class="text-lg font-semibold">{{ task.title }}</h3>
                <p class="text-sm text-gray-600">{{ task.description }}</p>
                <p class="text-sm text-gray-500">Due: {{ task.due_date }}</p>
              </div>
              <span
                :class="{
                  'bg-green-200 text-green-800': task.status,
                  'bg-red-200 text-red-800': !task.status,
                }"
                class="px-3 py-1 rounded-full text-sm"
              >
                {{ task.status ? 'Completed' : 'Pending' }}
              </span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { ref, onMounted } from 'vue';
  import api from '@/services/api';
  
  export default {
    setup() {
      const tasks = ref([]);
  
      const fetchTasks = async () => {
        try {
          const response = await api.get('/tasks/');
          tasks.value = response.data;
        } catch (error) {
          console.error('Failed to fetch tasks:', error);
        }
      };
  
      onMounted(() => {
        fetchTasks();
      });
  
      return { tasks };
    },
  };
  </script>