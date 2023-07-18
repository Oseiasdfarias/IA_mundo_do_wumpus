// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/palenight');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Mundo do Wumpus - IA',
  tagline: 'Ambiente para estudos de Inteligência Computacional',
  favicon: 'img/favicon_1.ico',

  // Set the production url of your site here
  url: 'https://oseiasdfarias.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/IA_mundo_do_wumpus/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Oseiasdfarias', // Usually your GitHub org/user name.
  projectName: 'IA_mundo_do_wumpus', // Usually your repo name.
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          //editUrl:
          //  'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Mundo do Wumpus - IA',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo_1.svg',
        },
        hideOnScroll: true,
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Relatório',
          },
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentação',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://pypi.org/project/ia-wumpus/',
            label: 'PyPI',
            position: 'right',
          },
          {
            href: 'https://github.com/Oseiasdfarias/IA_mundo_do_wumpus',
            label: 'GitHub',
            position: 'right',
          },
          {
            type: 'search',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        logo: {
          alt: 'O Mundo do Wumpus',
          src: 'img/logo_1.svg',
          href: 'https://oseiasdfarias.github.io/IA_mundo_do_wumpus/',
          width: 160,
          height: 100,
        },
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Relatório',
                to: '/docs/category/Relatório',
              },
              {
                label: 'Documentação',
                to: '/docs/category/Documentação',
              },
            ],
          },
          {
            title: 'Comunicação',
            items: [
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/docusaurus',
              },
            ],
          },
          {
            title: 'Mais',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/Oseiasdfarias/IA_mundo_do_wumpus',
              },
              {
                label: 'PyPI',
                href: 'https://pypi.org/project/ia-wumpus/',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} ia-wumpus, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
