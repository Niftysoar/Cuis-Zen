import Route from "./Route.js";

//Définir ici vos routes
export const allRoutes = [
    new Route("/", "Accueil", "/pages/home.html", []),
    new Route("/about", "A propos", "/pages/about.html", []),
    new Route("/lives", "Lives", "/pages/events.php", []),
    new Route("/contact", "Contact", "/pages/contact.html", []),
];

//Le titre s'affiche comme ceci : Route.titre - websitename
export const websiteName = "Cuis'zen";