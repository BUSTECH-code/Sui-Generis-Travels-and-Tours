import { API } from './api.js';

export const Gallery = {
  async init() {
    gsap.registerPlugin(ScrollTrigger);
    await this.renderGallery();
  },

  async renderGallery() {
    const container = document.getElementById('gallery-container');
    if (!container) return;

    try {
      const items = await API.getGalleryItems();
      
      const fallbackItems = [
        { title: "UK Student Visa Success", image_url: "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=600&q=80", category: "Study" },
        { title: "Dubai Group Holiday", image_url: "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=600&q=80", category: "Tours" },
        { title: "Canada Admission Arrival", image_url: "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=600&q=80", category: "Study" },
        { title: "Executive Business Flight", image_url: "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=600&q=80", category: "Flights" }
      ];

      const displayList = (items && items.length > 0) ? items : fallbackItems;

      container.innerHTML = displayList.map(item => `
        <div class="gallery-card gsap-card">
          <img src="${item.image_url}" alt="${item.title}">
          <div class="gallery-overlay">
            <h4 style="margin: 0; font-size: 1.1rem;">${item.title}</h4>
            <span style="font-size: 0.8rem; color: var(--accent-gold);">${item.category || 'Travel'}</span>
          </div>
        </div>
      `).join('');

      // Trigger GSAP Scrollytelling Entrance
      gsap.from(".gsap-card", {
        duration: 0.8,
        y: 50,
        opacity: 0,
        stagger: 0.15,
        ease: "power2.out",
        scrollTrigger: {
          trigger: "#gallery-container",
          start: "top 80%"
        }
      });

    } catch (err) {
      console.warn('Gallery fallback rendering activated');
    }
  }
};

document.addEventListener('DOMContentLoaded', () => Gallery.init());