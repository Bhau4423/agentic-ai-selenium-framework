from pathlib import Path


class BaseTestGenerator:

    @staticmethod
    def generate():

        lines = []

        lines.append(
            "package base;"
        )

        lines.append("")

        lines.append(
            "import java.io.FileInputStream;"
        )

        lines.append(
            "import java.io.IOException;"
        )

        lines.append(
            "import java.time.Duration;"
        )

        lines.append(
            "import java.util.Properties;"
        )

        lines.append(
            "import org.openqa.selenium.WebDriver;"
        )

        lines.append(
            "import org.openqa.selenium.chrome.ChromeDriver;"
        )

        lines.append(
            "import org.openqa.selenium.support.ui.WebDriverWait;"
        )

        lines.append(
            "import org.testng.annotations.AfterMethod;"
        )

        lines.append(
            "import org.testng.annotations.BeforeMethod;"
        )

        lines.append("")

        lines.append(
            "public class BaseTest {"
        )

        lines.append("")

        lines.append(
            "    protected WebDriver driver;"
        )

        lines.append(
            "    protected WebDriverWait wait;"
        )

        lines.append(
            "    protected Properties properties;"
        )

        lines.append("")

        lines.append(
            "    @BeforeMethod"
        )

        lines.append(
            "    public void setup() throws IOException {"
        )

        lines.append("")

        lines.append(
            '        properties = new Properties();'
        )

        lines.append(
            '        properties.load('
        )

        lines.append(
            '            new FileInputStream('
        )

        lines.append(
            '                "generated_framework/config/config.properties"'
        )

        lines.append(
            '            )'
        )

        lines.append(
            '        );'
        )

        lines.append("")

        lines.append(
            '        String browser ='
        )

        lines.append(
            '            properties.getProperty("browser");'
        )

        lines.append("")

        lines.append(
            '        String baseUrl ='
        )

        lines.append(
            '            properties.getProperty("baseUrl");'
        )

        lines.append("")

        lines.append(
            '        int timeout = Integer.parseInt('
        )

        lines.append(
            '            properties.getProperty("timeout")'
        )

        lines.append(
            '        );'
        )

        lines.append("")

        lines.append(
            '        if('
        )

        lines.append(
            '            browser.equalsIgnoreCase("chrome")'
        )

        lines.append(
            '        ) {'
        )

        lines.append(
            '            driver = new ChromeDriver();'
        )

        lines.append(
            '        }'
        )

        lines.append("")

        lines.append(
            '        driver.manage()'
        )

        lines.append(
            '              .window()'
        )

        lines.append(
            '              .maximize();'
        )

        lines.append("")

        lines.append(
            '        wait = new WebDriverWait('
        )

        lines.append(
            '            driver,'
        )

        lines.append(
            '            Duration.ofSeconds(timeout)'
        )

        lines.append(
            '        );'
        )

        lines.append("")

        lines.append(
            '        driver.get(baseUrl);'
        )

        lines.append(
            '    }'
        )

        lines.append("")

        lines.append(
            '    @AfterMethod'
        )

        lines.append(
            '    public void teardown() {'
        )

        lines.append(
            '        if(driver != null) {'
        )

        lines.append(
            '            driver.quit();'
        )

        lines.append(
            '        }'
        )

        lines.append(
            '    }'
        )

        lines.append("")

        lines.append(
            "}"
        )

        return "\n".join(lines)

    @staticmethod
    def save():

        output_dir = Path(
            "generated_framework/base"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            output_dir
            / "BaseTest.java"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                BaseTestGenerator.generate()
            )

        return str(file_path)