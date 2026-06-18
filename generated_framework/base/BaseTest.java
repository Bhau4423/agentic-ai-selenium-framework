package base;

import java.io.FileInputStream;
import java.io.IOException;
import java.time.Duration;
import java.util.Properties;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;

public class BaseTest {

    protected WebDriver driver;
    protected WebDriverWait wait;
    protected Properties properties;

    @BeforeMethod
    public void setup() throws IOException {

        properties = new Properties();
        properties.load(
            new FileInputStream(
                "generated_framework/config/config.properties"
            )
        );

        String browser =
            properties.getProperty("browser");

        String baseUrl =
            properties.getProperty("baseUrl");

        int timeout = Integer.parseInt(
            properties.getProperty("timeout")
        );

        if(
            browser.equalsIgnoreCase("chrome")
        ) {
            driver = new ChromeDriver();
        }

        driver.manage()
              .window()
              .maximize();

        wait = new WebDriverWait(
            driver,
            Duration.ofSeconds(timeout)
        );

        driver.get(baseUrl);
    }

    @AfterMethod
    public void teardown() {
        if(driver != null) {
            driver.quit();
        }
    }

}