package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.CheckboxesPage;

public class InteractWithDisabledCheckboxTest extends BaseTest {

    @Test
    public void interactWithDisabledCheckbox() {

        CheckboxesPage page = new CheckboxesPage(driver);

        wait.until(ExpectedConditions.elementToBeClickable(page.get_checkbox_0()));
        page.get_checkbox_0().click();

        wait.until(ExpectedConditions.visibilityOf(page.get_checkbox_0()));
        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}