import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "Sonny",
      logo: {
        light: "./src/assets/light-logo.svg",
        dark: "./src/assets/dark-logo.svg",
        replacesTitle: true,
      },
      social: {
        twitch: "https://twitch.tv/superp0sit1on",
        github: "https://github.com/superp0sit1on/sonny",
      },
      sidebar: [
        {
          label: "Start Here",
          items: [
            { label: "Getting Started", link: "/getting-started" },
            { label: "Releases Notes", link: "/releases" },
          ],
        },
        {
          label: "Guides",
          items: [
            { label: "Project Structure", link: "/guides/project-structure" },
            { label: "Writing Commands", link: "/guides/writing-commands" },
            {
              label: "Managing Modules",
              link: "/guides/managing-modules",
            },
            { label: "Deploy to Heroku", link: "/guides/deploy-to-heroku" },
            {
              label: "Documenting",
              link: "/guides/documenting",
            },
            { label: "Contributing", link: "/guides/contributing" },
          ],
        },
        {
          label: "Resources",
          autogenerate: { directory: "resources" },
        },
      ],
    }),
  ],
});
