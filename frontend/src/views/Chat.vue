<script setup lang="ts">
</script>

<template>
<main class="flex flex-col justify-center m-auto md:w-7/12 mt-5 gap-2">
  <div class="relative flex flex-col text-white py-2 bg-slate-700 rounded-lg">
    <div class="px-2">
      FooBar
    </div>
  </div>
  <div class="relative flex flex-col text-white py-2 bg-slate-500 rounded-lg">
    <div class="px-2">
      Lorem Ipsum
    </div>
  </div>
  <div class="relative flex flex-col text-white py-2 bg-slate-500 rounded-lg">
  <video controls>
    <source src="@/assets/rabbit320.mp4" type="video/mp4" />
  </video>
  </div>
  <div class="relative flex flex-col">
    <textarea type="text" class="w-full rounded bg-slate-800 py-1 pl-2 text-white focus:outline-none focus:ring focus:ring-violet-400 resize-y" placeholder="Text"></textarea>
  </div>
</main>
</template>
