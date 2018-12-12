#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to a pointer to the first node in the list
 * Return: a 0 if it is not a palindrome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	if (is_palindrome_check(*head, tmp))
		return (1);
	else
		return (0);
}

/**
 * is_palindrome_check - checks if a linked list is a palindrome
 * @head: a pointer to the first element of a list
 * @tmp: a pointer to be iterated
 * Return: a null pointer if not a palindrome and not null if palindrome
 */
listint_t *is_palindrome_check(listint_t *head, listint_t *tmp)
{
	listint_t *ret;

	if (tmp == NULL)
		return (head);
	else
	{
		ret = is_palindrome_check(head, tmp->next);
		if (ret == NULL)
			return (NULL);
		if (ret->n == tmp->n && ret->next)
			return (ret->next);
		else if (ret->n == head->n)
			return (ret);
		else
			return (NULL);
	}
	return (NULL);
}
