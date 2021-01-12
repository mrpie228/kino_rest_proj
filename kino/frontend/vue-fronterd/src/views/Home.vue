<template>

<section class="main-container" >
      <div class="location" id="home">
          <h1 id="home">Рекомендуем:</h1>
          <div   class="box rec_movies">
            <a v-for="movie in movies" v-bind:key="movie.id" ><img :src="movie.poster" alt="" @click="goToMovie(movie.url)" ><br></a>
          </div>
          <h1 id="tvShows">Категории:</h1>
      <div class="box category">
        <a v-for="category in categories" v-bind:key="category.id" ><img :src="category.poster" alt="" @click="goToCategory(category.url)"></a>
       
      </div>
      </div>
</section>

</template>


<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
  },
  data(){
    return{
      movies:[],
      categories:[],
    }
  },
    created() {
      this.loadMovies(),
      this.loadCategoty()
    },
  methods: {
    async loadMovies(){
      this.movies = await fetch(
        `http://127.0.0.1:8000/api/v2/movie/`
      ).then(response=>response.json())
    },
    async loadCategoty(){
      this.categories = await fetch(
        `http://127.0.0.1:8000/api/v2/categories/`
      ).then(response=>response.json())
    },
 
    goToMovie(url){
      this.$router.push({name:"OneMovie", params: {url:url} })
    },
    goToCategory(name){
      this.$router.push({name:"OneCategory", params: {name:name} })
    }
   },
  }

</script>
