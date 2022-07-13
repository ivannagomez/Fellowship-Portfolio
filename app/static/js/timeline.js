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
        <h5 style="line-height:0.4">${post['name']}</h5>
        <li style="line-height:2.6">Content: ${post['content']}</il>
        <p style="line-height:0.6">${post['email']}</p>
        <p style="line-height:0.4">${post['created_at']}</p>
        <p style="line-height:1.6"><br></p>
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
