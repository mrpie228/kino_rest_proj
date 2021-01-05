<template>

<section class="main-container" >
     <div class="location" id="home">
          <h1 id="home">Рекомендуем:</h1>
          <div   class="box">
            <a v-bind:key="movie.id" ><img :src="movie.poster" alt="" ><br></a>
          </div>
      </div>

</section>

  <!--<div v-for="movie in movies" v-bind:key="movie.id">
  <a>{{movie.title}}</a>
  <a> {{movie.middle_rating}}</a>
  <a> {{movie.that_user_rating}}</a>
  </div>
  </div>-->

</template>


<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'OneMovie',
  props:['url'],
  data(){
    return{
      movie:{}
    }
  },
  created() {
      this.loadMovie()
    },
  methods: {
    async loadMovie(){
      this.movie = await fetch(
        `http://localhost:8000/api/v2/movie/${this.url}`
      ).then(response=>response.json())
    }
  }
}

</script>
