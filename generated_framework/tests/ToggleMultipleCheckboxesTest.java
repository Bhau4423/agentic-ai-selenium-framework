package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.CheckboxesPage;

public class ToggleMultipleCheckboxesTest extends BaseTest {

    @Test
    public void toggleMultipleCheckboxes() {

        CheckboxesPage page = new CheckboxesPage(driver);

        wait.until(ExpectedConditions.elementToBeClickable(page.get_checkbox_0()));
        page.get_checkbox_0().click();

        wait.until(ExpectedConditions.elementToBeClickable(page.get_checkbox_1()));
        page.get_checkbox_1().click();

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}