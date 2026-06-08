public class HomeController : Controller
{
    public IActionResult Index()
    {
    ViewBag.Title = "Home";
        return View();
    }
}
Public
