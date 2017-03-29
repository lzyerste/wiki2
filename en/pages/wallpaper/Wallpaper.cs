using System;
using System.IO;
using System.Runtime.InteropServices;
using Microsoft.Win32;

public sealed class Wallpaper {
    Wallpaper() { }

    public static string PATH = "./";

    public static void Main(string[] args) {
        System.Console.WriteLine("Change wallpaper.");
        string fpath = PATH + "today.jpg"; // default
        if (args.Length > 0) {
            fpath = args[0].ToString();
        }
        Wallpaper.Set(fpath, Style.Stretched);
        // Wallpaper.Set("https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png", Style.Stretched);
    }

    const int SPI_SETDESKWALLPAPER = 20;
    const int SPIF_UPDATEINIFILE = 0x01;
    const int SPIF_SENDWININICHANGE = 0x02;

    [DllImport("user32.dll", CharSet = CharSet.Auto)]
    static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);

    public enum Style : int {
        Tiled,
        Centered,
        Stretched
    }

    public static void Set(string uri, Style style) {
        string tempPath = uri;
        if (uri.StartsWith("http")) {
            System.IO.Stream s = new System.Net.WebClient().OpenRead(uri);

            System.Drawing.Image img = System.Drawing.Image.FromStream(s);
            tempPath = Path.Combine(Path.GetTempPath(), PATH + "wallpaper.jpg");
            img.Save(tempPath, System.Drawing.Imaging.ImageFormat.Jpeg);
        }

        // string tempPath = Path.Combine(Path.GetTempPath(), uri.ToString());
        System.Console.WriteLine(tempPath);
        // tempPath = PATH + "today.jpg";

        RegistryKey key = Registry.CurrentUser.OpenSubKey(@"Control Panel\Desktop", true);
        if (style == Style.Stretched) {
            key.SetValue(@"WallpaperStyle", 2.ToString());
            key.SetValue(@"TileWallpaper", 0.ToString());
        }

        if (style == Style.Centered) {
            key.SetValue(@"WallpaperStyle", 1.ToString());
            key.SetValue(@"TileWallpaper", 0.ToString());
        }

        if (style == Style.Tiled) {
            key.SetValue(@"WallpaperStyle", 1.ToString());
            key.SetValue(@"TileWallpaper", 1.ToString());
        }

        SystemParametersInfo(SPI_SETDESKWALLPAPER,
            0,
            tempPath,
            SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE);
    }
}