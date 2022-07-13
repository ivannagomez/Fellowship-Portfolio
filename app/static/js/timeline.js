const posts = document.querySelector('#posts');

const getPosts = () => {
    fetch('/api/timeline_post')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const posts_data = data['timeline_posts']
            const html = posts_data.map(post2html).join('\n');
            posts.innerHTML = html;
        }
        );
    
}
const post2html = (post) =>{
    return `
        <li>Name: ${post['name']},
            Email: ${post['email']}, 
            Content: ${post['content']}</il>
        `
}

getPosts();

const form = document.querySelector('#form');
 
form.addEventListener('submit', function(e) {
    console.log('listening for form data')
    
    e.preventDefault();
    
    const formData = new FormData(form);
    console.log(formData)
    const payload = new URLSearchParams(formData);
    console.log(payload)
    fetch('/api/timeline_post', {
        method: 'POST',
        body: payload,
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        getPosts();
    })
})
