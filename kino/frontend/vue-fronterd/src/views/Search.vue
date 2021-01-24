<template>
<section class="main-container" >
  <div class="search">
    <h1>This is an search page</h1>
    <form >
      <input v-model="message" placeholder="Search something..." />
      <button>sumbit</button><br>
      <input type="checkbox" v-model="toggle" true-value="yes" false-value="no" />
      
    </form>
    <h2>{{message}}</h2>
  </div>
</section>
</template>
